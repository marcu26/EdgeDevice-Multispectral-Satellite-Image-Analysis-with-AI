using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace MicroControllersAPI.Migrations
{
    public partial class ModifiedAnalizeResults : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "Location",
                table: "AnalizeResults",
                type: "nvarchar(max)",
                nullable: false,
                defaultValue: "");

            migrationBuilder.AddColumn<string>(
                name: "MicrocontrollerName",
                table: "AnalizeResults",
                type: "nvarchar(max)",
                nullable: false,
                defaultValue: "");
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "Location",
                table: "AnalizeResults");

            migrationBuilder.DropColumn(
                name: "MicrocontrollerName",
                table: "AnalizeResults");
        }
    }
}
