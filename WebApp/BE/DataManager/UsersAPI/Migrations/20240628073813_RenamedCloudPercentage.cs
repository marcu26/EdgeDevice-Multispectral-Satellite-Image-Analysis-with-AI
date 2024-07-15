using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace MicroControllersAPI.Migrations
{
    public partial class RenamedCloudPercentage : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.RenameColumn(
                name: "CloudPercentage",
                table: "AnalizeResults",
                newName: "UnusablePercentage");
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.RenameColumn(
                name: "UnusablePercentage",
                table: "AnalizeResults",
                newName: "CloudPercentage");
        }
    }
}
