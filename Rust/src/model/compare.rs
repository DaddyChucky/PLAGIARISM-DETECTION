/// Pairwise comparison between all preprocessed files.
use super::constant::OUTPUT_FOLDER;
use anyhow::Result;
use rayon::prelude::*;
use std::{
    fs,
    sync::{Arc, Mutex},
};

pub fn compare_all(minimum_match: usize) -> Result<Vec<(String, f64)>> {
    let output = fs::read_dir(OUTPUT_FOLDER)?;
    let mut files = vec![];
    for entry in output {
        let Ok(entry) = entry else {continue};
        files.push((entry.path(), fs::read_to_string(entry.path()).unwrap()));
    }
    if files.len() == 0 {
        return Ok(vec![]);
    }
    let result = Arc::new(Mutex::new(Vec::new()));
    (0..(files.len() - 1))
        .into_par_iter()
        .for_each_with(result.clone(), |result, i| {
            let text_a = &files[i].1;
            ((i + 1)..files.len())
                .into_par_iter()
                .for_each_with(result.clone(), |result, j| {
                    let text_b = &files[j].1;
                    let (text, pattern) = if text_a.len() > text_b.len() {
                        (&text_a, &text_b)
                    } else {
                        (&text_b, &text_a)
                    };
                    let matches = rkr_gst::run(
                        pattern.as_bytes(),
                        text.as_bytes(),
                        2 * minimum_match,
                        minimum_match,
                    );
                    if !matches.is_empty() {
                        let label = format!(
                            "{} {}",
                            files[i].0.file_name().unwrap().to_str().unwrap(),
                            files[j].0.file_name().unwrap().to_str().unwrap(),
                        );
                        let matches_sum = 2 * matches.iter().map(|x| x.length).sum::<usize>();
                        let total_sum = text.len() + pattern.len();
                        result
                            .lock()
                            .unwrap()
                            .push((label, matches_sum as f64 / total_sum as f64));
                    }
                });
        });
    Ok(Arc::try_unwrap(result).unwrap().into_inner().unwrap())
}
