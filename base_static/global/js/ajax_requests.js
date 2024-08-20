ajax_requests = {
    editTicketsApi:function(data_array, ajaxCallback){
        $.ajax({
            url:'http://127.0.0.1:8000/ticket/ticket_edit/',
            type:'GET',
            dataType:'json',
            data:{attribute_name:data_array['attribute_name'], ticket_id:data_array['ticket_id'], item_value:data_array['item_value']},
            success:function(json){
                work_desk_id = {}
                if(json){
                
                }else{
                    console.log("sem resposta")
                }
            }
        })
    }

    
}