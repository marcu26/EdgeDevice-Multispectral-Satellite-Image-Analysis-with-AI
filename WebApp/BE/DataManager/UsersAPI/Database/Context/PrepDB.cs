using Core.Utils;
using Microsoft.EntityFrameworkCore;

namespace MicroControllersAPI.Database.Context
{
    public class PrepDB
    {
        public static async Task PrepPopulation(IApplicationBuilder app)
        {
            using (var serviceScope = app.ApplicationServices.CreateScope())
            {
                await SeedData(serviceScope.ServiceProvider.GetService<DatabaseContext>());
            }
        }

        private static async Task SeedData(DatabaseContext context)
        {

            Console.WriteLine("--> Attempting to apply migrations...");
            try
            {
                await context.Database.MigrateAsync();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"--> Could not run migrations: {ex.Message}");
            }

            if (!context.Roles.Any())
            {
                context.Roles.AddRange
                    (
                    new Entities.Role {  IsDeleted = false, CreatedAt = DateTime.Now, Name = "Admin" },
                    new Entities.Role {  IsDeleted = false, CreatedAt = DateTime.Now, Name = "Viewer" },
                    new Entities.Role {  IsDeleted = false, CreatedAt = DateTime.Now, Name = "Editor" }
                    );
            }

            if (!context.Users.Any())
            {
                context.Users.Add(new Entities.User { CreatedAt = DateTime.Now, IsDeleted = false, Email = "admin@admin.ro", Password = Hasher.Sha256Hash("test"), RoleId = 1, FirstName="Admin", LastName = "Admin" });
            }

            await context.SaveChangesAsync();
        }

    }
}
