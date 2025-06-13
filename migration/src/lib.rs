pub use sea_orm_migration::prelude::*;

mod m20250612_134407_create_users;
mod m20250613_083617_seed_users;

pub struct Migrator;

#[async_trait::async_trait]
impl MigratorTrait for Migrator {
    fn migrations() -> Vec<Box<dyn MigrationTrait>> {
        vec![
            Box::new(m20250612_134407_create_users::Migration),
            Box::new(m20250613_083617_seed_users::Migration),
        ]
    }
}
