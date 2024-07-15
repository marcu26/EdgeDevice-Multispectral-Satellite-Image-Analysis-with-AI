using Microsoft.Extensions.Configuration;
using System.Configuration;
using MicroControllersAPI.Infrastructure.Config.ConfigModels;

namespace MicroControllersAPI.Infrastructure.Config
{
    public static class AppConfig
    {
        public static ConnectionStringsConfig ConnectionStringsConfig { get; set; }
        public static JwtConfiguration JwtConfiguration { get; set; }


        public static void Init(IConfiguration configuration)
        {
            var connectionStringConfig = configuration.GetSection("ConnectionStringsSettings");
            ConnectionStringsConfig = connectionStringConfig.Get<ConnectionStringsConfig>();

            var jwtConfig = configuration.GetSection("JwtConfiguration");
            JwtConfiguration = jwtConfig.Get<JwtConfiguration>();
        }
    }
}
