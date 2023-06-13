/// Main windows shown when executing the application
use super::graph::{chart, transform};
use super::task::Task;
use crate::model;
use anyhow::Result;
use eframe::egui::{self, plot::Bar, Slider, Ui};
use rfd::FileDialog;
use serde::{Deserialize, Serialize};

#[derive(Deserialize, Serialize, Default)]
#[serde(default)]
pub struct PlagiarismDetector {
    gitignore: String,
    input_dir: Option<String>,
    example_dir: Option<String>,
    preprocess_done: bool,
    result: Vec<(String, f64)>,
    minimum_match: usize,
    reset: bool,
    #[serde(skip)]
    promise_preprocess: Task<Result<()>>,
    #[serde(skip)]
    promise_compare: Task<Vec<Bar>>,
}

impl PlagiarismDetector {
    pub fn new(cc: &eframe::CreationContext<'_>) -> Self {
        if let Some(storage) = cc.storage {
            return eframe::get_value(storage, eframe::APP_KEY).unwrap_or_default();
        }
        Default::default()
    }

    fn layout(&mut self, ui: &mut Ui) {
        ui.heading("Preprocessing");
        ui.horizontal(|ui| {
            ui.add_sized(
                [0.42 * ui.available_width(), 70.0],
                egui::TextEdit::multiline(&mut self.gitignore)
                    .code_editor()
                    .hint_text(
                        "Write in a gitignore manner what files or folders should be excluded",
                    )
                    .desired_rows(7),
            );
            ui.vertical(|ui| {
                if ui.button("Input directory").clicked() {
                    if let Some(path) = FileDialog::new().set_directory(".").pick_folder() {
                        self.input_dir = Some(path.display().to_string());
                        self.preprocess_done = false;
                    }
                }
                if let Some(input_dir) = &self.input_dir {
                    ui.label(input_dir);
                }
                if ui.button("Skeleton directory").clicked() {
                    if let Some(path) = FileDialog::new().set_directory(".").pick_folder() {
                        self.example_dir = Some(path.display().to_string());
                    }
                }
                if let Some(example_dir) = &self.example_dir {
                    ui.label(example_dir);
                }
            });
        });
        if let (Some(input_dir), Some(example)) = (&self.input_dir, &self.example_dir) {
            let input_dir = input_dir.clone();
            let example = example.clone();
            let gitignore = self.gitignore.clone();
            let interior = || self.promise_compare = Task::NotStarted;
            let preprocess =
                move || model::preprocessing::preprocess(input_dir, example, gitignore);
            self.promise_preprocess
                .expensive_task_button(ui, "Preprocess", preprocess, interior);
            if let Some(result) = self.promise_preprocess.ready() {
                match result {
                    Ok(_) => self.preprocess_done = true,
                    Err(error) => println!("{}", error),
                }
            }
        }
        if !self.preprocess_done {
            return;
        }
        ui.heading("Find common occurence");
        ui.add(
            Slider::new(&mut self.minimum_match, 32..=2_usize.pow(15))
                .text("Minimum match length")
                .logarithmic(true),
        );
        let minimum_match = self.minimum_match;
        let compare_fn = move || transform(model::compare::compare_all(minimum_match).unwrap());
        let interior_fn = || self.reset = true;
        self.promise_compare
            .expensive_task_button(ui, "Compare", compare_fn, interior_fn);
        if let Some(result) = self.promise_compare.ready() {
            chart(ui, result, &mut self.reset);
        }
    }
}

impl eframe::App for PlagiarismDetector {
    fn save(&mut self, storage: &mut dyn eframe::Storage) {
        eframe::set_value(storage, eframe::APP_KEY, self);
    }

    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            egui::ScrollArea::vertical().show(ui, |ui| {
                self.layout(ui);
            });
        });
    }
}
