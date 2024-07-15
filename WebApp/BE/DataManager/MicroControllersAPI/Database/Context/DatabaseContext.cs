using Microsoft.EntityFrameworkCore;
using MicroControllersAPI.Infrastructure.Config;
using MicroControllersAPI.Database.Entities;

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

        public DbSet<AnalizeResult> AnalizeResults { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            
        }
    }
}
