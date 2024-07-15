using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.IdentityModel.Tokens;
using Microsoft.OpenApi.Models;
using System.Text;
using MicroControllersAPI.Database.Context;
using MicroControllersAPI.Infrastructure.Config;
using MicroControllersAPI.Repos;
using MicroControllersAPI.Services;

namespace Core.Extensions
{
    public static class IServiceCollectionExtensions
    {
        public static void AddContext(this IServiceCollection services)
        {
            services.AddDbContext<DatabaseContext>();
        }
        public static void AddRepositories(this IServiceCollection services)
        {
            services.AddScoped<AnalizeResultsRepo>();
        }

        public static void AddServices(this IServiceCollection services)
        {
            services.AddScoped<AnalizeResultsService>();
            services.AddSignalR();
        }

        public static void ConfigureSwagger(this IServiceCollection services)
        {
            services.AddSwaggerGen(options =>
            {
                options.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme
                {
                    Description = "Standard Authorization header using the Bearer scheme (bearer {token})",
                    In = ParameterLocation.Header,
                    Name = "Authorization",
                    Type = SecuritySchemeType.Http,
                    Scheme = "Bearer"
                });
                options.AddSecurityRequirement(new OpenApiSecurityRequirement()
                {
                    {
                        new OpenApiSecurityScheme
                        {
                            Reference = new OpenApiReference
                            {
                                Type = ReferenceType.SecurityScheme,
                                Id = "Bearer"
                            },
                            In = ParameterLocation.Header,
                        }, new List<string>()
                    }
                });


            });
        }
        public static void ConfigureAuthorization(this IServiceCollection services)
        {
            services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
                .AddJwtBearer(options =>
                {
                    options.TokenValidationParameters = new TokenValidationParameters
                    {
                        ValidateIssuerSigningKey = true,
                        IssuerSigningKey = new SymmetricSecurityKey(
                            Encoding.UTF8.GetBytes(AppConfig.JwtConfiguration.SecretKey)),
                        ValidateIssuer = true,
                        ValidateAudience = true,
                        ValidateLifetime = true,
                        ValidAudience = AppConfig.JwtConfiguration.Audience,
                        ValidIssuer = AppConfig.JwtConfiguration.Issuer,
                        ClockSkew = TimeSpan.Zero
                    };
                });
        }
    }
}
