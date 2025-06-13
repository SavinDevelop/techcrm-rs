use serde::Deserialize;
use config::{Config, Environment};
use dotenvy::dotenv;
use once_cell::sync::Lazy;

#[derive(Debug, Deserialize)]
pub struct AppSettings {
    pub port: u16,
    pub database_url: String,
}

impl AppSettings {
    pub fn load() -> Self {
        dotenv().ok();

        let config = Config::builder()
            .add_source(Environment::default().try_parsing(true))
            .build()
            .expect("Failed to build config");

        config.try_deserialize().expect("Invalid config format")
    }
}

pub static SETTINGS: Lazy<AppSettings> = Lazy::new(|| AppSettings::load());
