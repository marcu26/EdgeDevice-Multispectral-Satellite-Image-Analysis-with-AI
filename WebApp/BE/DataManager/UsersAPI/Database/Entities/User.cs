using MicroControllersAPI.Infrastructure.Base;

namespace MicroControllersAPI.Database.Entities
{
    public class User : BaseEntity
    {
        public string Email { get; set; }   
        public string Password { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public long RoleId { get; set; }
        public Role Role { get; set; }
    }
}
