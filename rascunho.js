$.each(element['work_desk'], function(key, value) {
                            
    // $("#id_work_desk_id").find('option[value='+value+']').attr("disabled", "disabled")
    $.each($("#id_work_desk_id"), function(keyel, valueel){
        
        if($(this).find('option[value='+value+']').val()){
            
                
                // console.log("o valor do objeto atual é: "+$(this).val()+"e o valor do banco é: "+value) 
        }else{
               
        }
        // if($(this).find('option[value='+value+']')){
        //     console.log(value)
        //     // $(this).attr("disabled", "disabled")
        //     // $("#id_work_desk_id").find('option[value='+valsel+']').attr("disabled", "disabled")
        //     // 
        // }else{
        //     console.log("achou")
            
        // }
        
    })
    
    
    // $('#id_work_desk_id').append($('<option>').text(value).attr('value', key))                           
});