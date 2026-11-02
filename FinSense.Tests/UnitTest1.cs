using FinSense;
using System.Text;
namespace FinSense.Tests;
public class LogicTests {
 [Fact] public void MoneyMustBePositiveAndCategoryMustMatch(){var a=new Account{Active=true};var m=new Movement{Date=new DateOnly(2025,1,1),Description="Compra",Type="gasto",Amount=0};Assert.NotNull(Logic.Validate(m,a,null));m.Amount=10;m.CategoryId=1;Assert.NotNull(Logic.Validate(m,a,new Category{Type="ingreso"}));Assert.Null(Logic.Validate(m,a,new Category{Type="gasto"}));}
 [Fact] public void RulesRespectPriorityAndMatchType(){Rule[] rules=[new(){Id=1,Active=true,Type="gasto",Pattern="cafe",Priority=20},new(){Id=2,Active=true,Type="gasto",Pattern="CAFE",Match="exacta",Priority=10}];Assert.Equal(2,Logic.MatchRule(rules,"cafe","gasto")!.Id);Assert.Equal(1,Logic.MatchRule(rules,"cafe central","gasto")!.Id);Assert.Null(Logic.MatchRule(rules,"cafe","ingreso"));}
 [Fact] public void CsvValidationRejectsMissingHeader(){Assert.Throws<ArgumentException>(()=>Logic.Parse(Encoding.UTF8.GetBytes("fecha,monto\n2025-01-01,2")));}
 [Fact] public void CsvExportEscapesFormula(){Assert.Equal("\"'=2+2\"",Logic.CsvSafe("=2+2"));Assert.Equal("\"hello\"\"world\"",Logic.CsvSafe("hello\"world"));}
 [Fact] public void ForecastRequiresHistory(){var result=ForecastService.Run([],new DateOnly(2026,11,1));Assert.Contains("No hay gastos",System.Text.Json.JsonSerializer.Serialize(result));}
}
