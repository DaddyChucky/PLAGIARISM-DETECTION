#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")] // hide console window on Windows in release

mod model;
mod view;

use anyhow::Result;
use view::app::PlagiarismDetector;

fn main() -> Result<(), eframe::Error> {
    env_logger::init(); // Log to stderr (if you run with `RUST_LOG=debug`).
    let options = eframe::NativeOptions::default();
    eframe::run_native(
        "Plagiarism detector",
        options,
        Box::new(|cc| Box::new(<PlagiarismDetector>::new(cc))),
    )
}
