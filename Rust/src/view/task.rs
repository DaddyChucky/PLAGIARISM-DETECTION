/// Button that execute an expensive task without blocking the rendering thread or necessiting a asynchronous framework like Tokio
use eframe::egui::{Button, Ui};
use std::sync::mpsc::Receiver;

pub enum Task<T: Send + Sync + 'static> {
    NotStarted,
    Pending(Receiver<T>),
    Ready(T),
}

impl<T: Send + Sync + 'static> Default for Task<T> {
    fn default() -> Self {
        Task::NotStarted
    }
}

impl<T: Send + Sync + 'static> Task<T> {
    /// Must not be called twice when the Status is still pending, but this is the job of expensive_task_button
    fn spawn_thread<Str, F>(&mut self, thread_name: Str, f: F)
    where
        Str: Into<String>,
        F: FnOnce() -> T + Send + Sync + 'static,
    {
        let (tx, rx) = std::sync::mpsc::channel();
        std::thread::Builder::new()
            .name(thread_name.into())
            .spawn(move || tx.send(f()))
            .expect("Failed to spawn thread");
        *self = Task::Pending(rx);
    }
    pub fn expensive_task_button<Str, F1, F2>(
        &mut self,
        ui: &mut Ui,
        button_name: Str,
        expensive_fn: F1,
        interior_fn: F2,
    ) where
        Str: Into<String>,
        F1: FnOnce() -> T + Send + Sync + 'static,
        F2: FnOnce(),
    {
        let is_ready = match self {
            Task::NotStarted => true,
            Task::Pending(_) => false,
            Task::Ready(_) => true,
        };
        let name = button_name.into();
        ui.add_enabled_ui(is_ready, move |ui| {
            let button = ui.add_sized([ui.available_width(), 40.0], Button::new(name.clone()));
            if button.clicked() {
                interior_fn();
                self.spawn_thread(name, expensive_fn);
            }
        });
    }
    fn poll(&mut self) {
        if let Task::Pending(ref rx) = self {
            if let Ok(value) = rx.try_recv() {
                *self = Task::Ready(value);
            }
        }
    }
    pub fn ready(&mut self) -> Option<&T> {
        self.poll();
        match self {
            Task::NotStarted => None,
            Task::Pending(_) => None,
            Task::Ready(ref value) => Some(value),
        }
    }
}
