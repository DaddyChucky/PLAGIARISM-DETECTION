use anyhow::Result;
use ignore::{
    gitignore::{Gitignore, GitignoreBuilder},
    Match,
};
use rayon::prelude::*;
use std::{fs, path::Path};

use super::constant::OUTPUT_FOLDER;

fn merge_dir_to_string(dir: &Path, result: &mut Vec<u8>, gitignore: &Gitignore) {
    if !dir.is_dir() {
        return;
    }
    if let Match::Ignore(_) = gitignore.matched(dir, true) {
        return;
    }
    let Ok(dir) = fs::read_dir(dir) else {return};
    for entry in dir {
        let Ok(entry) = entry else {continue};
        let path = entry.path();
        if let Match::Ignore(_) = gitignore.matched(&path, path.is_dir()) {
            continue;
        }
        if path.is_dir() {
            merge_dir_to_string(&path, result, gitignore);
        } else if path.is_file() {
            let Ok(file_content) = fs::read_to_string(path) else {continue};
            file_content
                .chars()
                .filter(|x| x.is_ascii())
                .map(|x| x as u8)
                .for_each(|x| result.push(x));
        }
    }
}

fn exclude_common_match(example: &[u8], student_content: &[u8]) -> Vec<u8> {
    let mut results = rkr_gst::run(example, student_content, 64, 32);
    results.sort_by_key(|x| x.text_index);
    let mut new_student_content = vec![];
    let mut i = 0;
    if results.is_empty() {
        new_student_content = student_content.to_vec();
    }
    for result in results.iter() {
        i += result.text_index;
        new_student_content.extend_from_slice(&student_content[i..i + result.length]);
        i += result.length;
    }
    new_student_content
}

pub fn preprocess(root_dir: String, example: String, gitignore_text: String) -> Result<()> {
    let _ = fs::remove_dir_all(OUTPUT_FOLDER);
    fs::create_dir(OUTPUT_FOLDER)?;
    let mut example_content = vec![];
    let mut gitignore = GitignoreBuilder::new(".");
    for line in gitignore_text.lines() {
        let _ = gitignore.add_line(None, line);
    }
    let gitignore = gitignore.build()?;
    merge_dir_to_string(Path::new(&example), &mut example_content, &gitignore);
    let root_dir = fs::read_dir(root_dir)?;
    root_dir.par_bridge().for_each(|entry| {
        let Ok(entry) = entry else {return};
        let mut student_content = vec![];
        let mut gitignore = GitignoreBuilder::new(entry.path());
        for line in gitignore_text.lines() {
            let _ = gitignore.add_line(None, line);
        }
        let Ok(gitignore) = gitignore.build() else {return};
        merge_dir_to_string(&entry.path(), &mut student_content, &gitignore);
        let student_content = exclude_common_match(&example_content, &student_content);
        let _ = fs::write(
            format!(
                "{}/{}.txt",
                OUTPUT_FOLDER,
                entry.file_name().to_str().unwrap()
            ),
            student_content,
        );
    });
    Ok(())
}
