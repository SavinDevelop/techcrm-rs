use sea_orm_migration::prelude::*;
use sea_orm_migration::sea_orm::{entity::*, query::*, Set};
use entity::users;

#[derive(DeriveMigrationName)]
pub struct Migration;

#[async_trait::async_trait]
impl MigrationTrait for Migration {
    async fn up(&self, manager: &SchemaManager) -> Result<(), DbErr> {
        let db = manager.get_connection();

        // простий хеш — у продакшн не використовувати
        let hash = hash_password("admin123");

        let users = users::ActiveModel {
            email: Set("admin@example.com".to_owned()),
            password_hash: Set(hash),
            ..Default::default()
        };

        users.insert(db).await?;

        Ok(())
    }

    async fn down(&self, manager: &SchemaManager) -> Result<(), DbErr> {
        let db = manager.get_connection();
        users::Entity::delete_many()
            .filter(users::Column::Email.eq("admin@example.com"))
            .exec(db)
            .await?;
        Ok(())
    }
}

// тимчасовий хешер (у продакшн використовуй Argon2, bcrypt тощо)
fn hash_password(password: &str) -> String {
    format!("hashed-{}", password)
}
