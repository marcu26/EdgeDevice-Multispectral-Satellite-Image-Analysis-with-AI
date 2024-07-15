using Microsoft.EntityFrameworkCore;
using MicroControllersAPI.Database.Entities;
using MicroControllersAPI.Infrastructure.Config;

namespace MicroControllersAPI.Database.Context
{
    public class DatabaseContext : DbContext
    {
        public DatabaseContext()
        {

        }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            base.OnConfiguring(optionsBuilder);
            optionsBuilder.UseSqlServer(AppConfig.ConnectionStringsConfig.MainDatabase);
        }

        public DbSet<User> Users { get; set; }
        public DbSet<Role> Roles { get; set; }
        public DbSet<AnalizeResult> AnalizeResults { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            
        }
    }
}
