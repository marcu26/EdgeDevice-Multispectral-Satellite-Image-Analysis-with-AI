namespace MicroControllersAPI.Infrastructure.Config.ConfigModels
{
    public class JwtConfiguration
    {
        public string SecretKey { get; set; }
        public string Issuer { get; set; }
        public string Audience { get; set; }
        public int JwtLifetimeInMonths { get; set; }
    }
}
