using Core.Extensions;
using MicroControllersAPI.Database.Context;
using MicroControllersAPI.Infrastructure.Config;

var builder = WebApplication.CreateBuilder(args);

AppConfig.Init(builder.Configuration);

// Add services to the container.

builder.Services.AddControllers();

builder.Services.AddCors(options =>
{
    options.AddDefaultPolicy(builder =>
    {
        builder.AllowAnyOrigin()
               .AllowAnyMethod()
               .AllowAnyHeader();
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


app.UseCors();

// Configure the HTTP request pipeline.
app.UseSwagger(c =>
{
    c.RouteTemplate = "api/swagger/{documentName}/swagger.json";
});

app.UseSwaggerUI(c =>
{
    c.SwaggerEndpoint("/api/swagger/v1/swagger.json", "UsersAPI");
    c.RoutePrefix = "api/swagger";
    c.DocumentTitle = $"UsersAPI {app.Environment.EnvironmentName} - Swagger UI";
});

app.UseHttpsRedirection();

app.UseAuthentication();
app.UseAuthorization();

app.MapControllers();

await PrepDB.PrepPopulation(app);

app.Run();
