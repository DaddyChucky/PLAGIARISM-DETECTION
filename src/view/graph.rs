use eframe::{
    egui::{
        plot::{Bar, BarChart, Legend, Plot},
        Response, Ui,
    },
    epaint::Color32,
};
use std::sync::{Arc, Mutex};

pub fn transform(data: Arc<Mutex<Vec<(String, f64)>>>) -> Vec<Bar> {
    let mut result = Arc::try_unwrap(data).unwrap().into_inner().unwrap();
    result.sort_by(|x, y| y.1.partial_cmp(&x.1).unwrap());

    result
        .iter()
        .enumerate()
        .map(|(i, (name, value))| Bar::new(i as f64 + 0.5, *value).name(name))
        .collect()
}

pub fn chart(ui: &mut Ui, result: &Vec<Bar>, reset: &mut bool) -> Response {
    let chart = BarChart::new(result.to_vec())
        .color(Color32::LIGHT_BLUE)
        .width(0.2)
        .name("Comparaison");
    let mut plot = Plot::new("Comparaison graphic");
    if *reset {
        *reset = false;
        plot = plot.reset();
    }
    plot.legend(Legend::default())
        .include_y(0.0)
        .include_y(1.0)
        .set_margin_fraction([2.0 / (result.len().pow(2)) as f32, 0.0].into())
        .allow_zoom(true)
        .allow_drag(true)
        .show(ui, |plot_ui| plot_ui.bar_chart(chart))
        .response
}
