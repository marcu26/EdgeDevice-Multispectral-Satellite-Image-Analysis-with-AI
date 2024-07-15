using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace MicroControllersAPI.Migrations
{
    public partial class RemoveUnnecessaryProperty : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "MicrocontrollerName",
                table: "AnalizeResults");
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "MicrocontrollerName",
                table: "AnalizeResults",
                type: "nvarchar(max)",
                nullable: false,
                defaultValue: "");
        }
    }
}
