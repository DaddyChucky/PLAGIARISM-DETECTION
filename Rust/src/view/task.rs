/// Button that execute an expensive task without blocking the rendering thread or necessiting a asynchronous framework like Tokio
use eframe::egui::{Button, Ui};
use poll_promise::Promise;

pub fn expensive_task_button<T: Send, F: FnOnce() -> T + Send + 'static, F2: FnOnce()>(
    ui: &mut Ui,
    promise: &mut Option<Promise<T>>,
    button_name: &str,
    function: F,
    interior: F2,
) {
    let is_ready = match promise {
        Some(promise) => promise.ready().is_some(),
        None => true,
    };
    ui.add_enabled_ui(is_ready, |ui| {
        if ui
            .add_sized([ui.available_width(), 40.0], Button::new(button_name))
            .clicked()
        {
            interior();
            *promise = Some(Promise::spawn_thread("thread", function));
        }
    });
}
