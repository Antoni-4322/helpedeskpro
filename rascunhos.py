



clients = tuple(Clients.objects.all().values())


clients = tuple(Clients.objects.all().values())
        org_list = {}
        delete = []
        new_list = {}
       
        for item in clients:
            item.update({'subs':[]})
            org_list[item['id']] = item
      
        
        new_list = org_list

        for key, values in org_list.items():
            for key_inner, values_inner in list(new_list.items()):
                
                if key == values_inner['sub_id_id']:
                    new_list[key]['subs'].append(values_inner)
                    delete.append(key_inner)
            
                    
        if delete:
            for i in delete:
                del new_list[i]
      
             
        pprint.pprint(new_list)