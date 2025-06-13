use tokio::sync::OnceCell;
use sea_orm::DatabaseConnection;

pub static DB: OnceCell<DatabaseConnection> = OnceCell::const_new();

use crate::settings::CONFIG;
use sea_orm::{ConnectOptions, Database};

pub async fn init_database() -> &'static DatabaseConnection {
    DB.get_or_init(|| async {
        let mut opt = ConnectOptions::new(CONFIG.database_url.clone());
        opt.sqlx_logging(true);
        Database::connect(opt).await.expect("DB connect failed")
    }).await
}
