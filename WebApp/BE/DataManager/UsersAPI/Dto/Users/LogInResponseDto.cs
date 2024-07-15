namespace MicroControllersAPI.Dto.Users
{
    public class LogInResponseDto
    {
        public long Id { get; set; } 
        public string Token { get; set; }
        public string UserName { get; set; }    
    }
}
