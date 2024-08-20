
$(function(){
    
    var url = window.location.pathname
    var ticket_id = $('#ticket_id').val()


    
    tickets_dashboard = $('.ticket-area-contents-a')


    $.each($('.ticket-area-contents-a'), function(){
        progress = $(this).attr('progress')
        $(this).find('.progress').css("width", progress+'%')
        console.log("achou")
        if (progress > 90){
            $(this).find('.progress').css("background-color", "#dd5035")
        }

    })     
    
   
    

    $('#id_category').on('change', function(){
        item_value = $(this).val()
        attribute_name = $(this).attr("name")
        data = {'item_value':item_value, 'ticket_id':ticket_id, 'attribute_name':attribute_name}
        ajax_requests.editTicketsApi(data, function(json){

        })  
    })

    $('#id_user').on('change', function(){
        item_value = $(this).val()
        attribute_name = $(this).attr("name")
        console.log(attribute_name)
        data = {'item_value':item_value, 'ticket_id':ticket_id, 'attribute_name':attribute_name}
        ajax_requests.editTicketsApi(data, function(json){

        })  
    })


    $('#id_work_desk_id').on('change', function(){
        item_value = $(this).val()
        attribute_name = $(this).attr("name")
        console.log(attribute_name)
        data = {'item_value':item_value, 'ticket_id':ticket_id, 'attribute_name':attribute_name}
        ajax_requests.editTicketsApi(data, function(json){

        })  
    })


    $('#id_ticket_type').on('change', function(){
        item_value = $(this).val()
        attribute_name = $(this).attr("name")
        console.log(attribute_name)
        data = {'item_value':item_value, 'ticket_id':ticket_id, 'attribute_name':attribute_name}
        ajax_requests.editTicketsApi(data, function(json){

        })  
    })


    $('#id_priority').on('change', function(){
        item_value = $(this).val()
        attribute_name = $(this).attr("name")
        console.log(attribute_name)
        data = {'item_value':item_value, 'ticket_id':ticket_id, 'attribute_name':attribute_name}
        ajax_requests.editTicketsApi(data, function(json){

        })  
    })


    $('#id_status').on('change', function(){
        item_value = $(this).val()
        attribute_name = $(this).attr("name")
        console.log(attribute_name)
        data = {'item_value':item_value, 'ticket_id':ticket_id, 'attribute_name':attribute_name}
        ajax_requests.editTicketsApi(data, function(json){

        })  
    })
   
    

    $('#id_user').on('change', function(){
        
        valsel = $(this).val()
        
        $.ajax({
            url:'http://127.0.0.1:8000/account/api/'+valsel+'',
            type:'GET',
            dataType:'json',
            success:function(json){
                work_desk_id = {}
                if(json){
                
                    json.forEach(element => {
                        work_desk_id = element['work_desk'] 
                    });
                    $("#id_work_desk_id").find('option').removeAttr("disabled")
                    $.each($("#id_work_desk_id").find('option'), function(){
                        if(work_desk_id.includes(parseInt($(this).val()))){
                            
                        }else{
                            $(this).attr("disabled", "disabled")
                        }
                    })      
                }else{
                    console.log("sem resposta")
                }
            }
        })
    })


   

    
    $('.section-projects--filters a').each(function(){
        
        if($(this).attr('href') == url){
            
            $(this).find('li').addClass("active")
        }

        var newstring = url.split('/')
        
        
        var hreflink = $(this).attr('href')
        // var newurl = hreflink.substring(hreflink.lastIndexOf("/"));
        // console.log(hreflink.replace(/\//g,''))
        
        if(newstring[1] == hreflink.replace(/\//g,'')){
            
            $(this).find('li').addClass("active")
        }
    })

    // a = $('.section-projects--filters a').attr('href')
    // console.log(a)
   
    
    $('.section-projects--filters li').on('click', function(e){
        // e.preventDefault();
        $('.section-projects--filters li').removeClass("active")
        $(this).addClass("active")
    })
})

