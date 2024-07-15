using Core.Extensions;
using MicroControllersAPI.Infrastructure.Config;
using MicroControllersAPI.Services;
using Microsoft.AspNetCore.Authentication;

var builder = WebApplication.CreateBuilder(args);

AppConfig.Init(builder.Configuration);

// Add services to the container.
builder.Services.AddControllers();

builder.Services.AddCors(options =>
{
    options.AddDefaultPolicy(policy =>
    {
        policy.WithOrigins("http://localhost:3000")
              .AllowAnyMethod()
              .AllowAnyHeader()
              .AllowCredentials();
    });

    options.AddDefaultPolicy(policy =>
    {
        policy.WithOrigins("https://localhost:3000")
              .AllowAnyMethod()
              .AllowAnyHeader()
              .AllowCredentials();
    });
});

builder.Services.AddContext();
builder.Services.AddRepositories();
builder.Services.AddServices();

builder.Services.ConfigureAuthorization();
builder.Services.ConfigureSwagger();

// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

app.UseHttpsRedirection();

app.UseStaticFiles();
app.UseDirectoryBrowser();

app.UseRouting();

app.UseCors();

app.UseAuthentication();
app.UseAuthorization();

// Configure the HTTP request pipeline.
app.UseSwagger(c =>
{
    c.RouteTemplate = "api/swagger/{documentName}/swagger.json";
});

app.UseSwaggerUI(c =>
{
    c.SwaggerEndpoint("/api/swagger/v1/swagger.json", "MicroControllersAPI");
    c.RoutePrefix = "api/swagger";
    c.DocumentTitle = $"MicroControllersAPI {app.Environment.EnvironmentName} - Swagger UI";
});

app.MapControllers();
app.MapHub<NotifyHub>("/notify");

app.Use(async (context, next) =>
{
    if (context.Request.Path.StartsWithSegments("/notify/negotiate"))
    {
        var authResult = await context.AuthenticateAsync();
        if (!authResult.Succeeded)
        {
            await context.ChallengeAsync();
            return;
        }
        else if (!context.User.Identity.IsAuthenticated)
        {
            context.Response.StatusCode = 401; // Unauthorized
            return;
        }
    }
    await next();
});

app.Run();
