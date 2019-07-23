$(function () {
 initprov();    
    
   
 
})

function initprov()
{
 		 $.post("/index.php/home/region/",{action:'get_prov','userid':userid},function(result){
                  
		  $("select[name='province']").html(result) ;     
           changeProvince($("select[name='province'] option:selected").val()); 
	
		})	
	
	
}
function changeProvince(provid)
{
	  
		
 		 $.post("/index.php/home/region/",{action:'get_city',provid:provid,'userid':userid},function(result){
                  
		  $("select[name='city']").html(result) ;     
          changeCity($("select[name='city'] option:selected").val()); 
	
		})	
	
	
}
function changeCity(cityid)
{
	  
		
 		 $.post("/index.php/home/region/",{action:'get_area',cityid:cityid,'userid':userid},function(result){
                  
		  $("select[name='area']").html(result) ;     

	
		})	
	
	
}