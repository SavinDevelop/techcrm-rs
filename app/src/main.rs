
mod settings;
mod db;

use settings::SETTINGS;
use db::init_database;

#[tokio::main]
async fn main() {
    let _ = init_database().await;

    println!("Server will run on port: {}", SETTINGS.port);
    println!("Database URL: {}", SETTINGS.database_url);
} 