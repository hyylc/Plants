//请求拦截器
import service from "../utils/request.js"


export function del_user(userinfo){
    return service.request({
        method : "post",
        url : "/delete_user",//对应flask里的路由
        data:{
            user_id : userinfo
        }
    });
};

export function del_plant(plantinfo){
    return service.request({
        method : "post",
        url : "/delete_plant",//对应flask里的路由
        data:{
            plant_id : plantinfo
        }
    });
};

export function do_login(userinfo){
    return service.request({
        method : "post",
        url : "/dologin",//对应flask里的路由
        data:{
            uname : userinfo.username,
            upwd : userinfo.password
        }
    });
};

export function do_register(userinfo){
    return service.request({
        method : "post",
        url : "/userloginup",//对应flask里的路由
        data:{
            uname : userinfo.username,
            upwd : userinfo.password
        }
    });
};

export function Get_header(){
    return service.request({
        method : "get",
        url : "/plants_header"//对应flask里的路由
    });
};

export function Get_order(){
    return service.request({
        method : "POST",
        url : "/order"//对应flask里的路由
    });
};

export function Get_family(){
    return service.request({
        method : "POST",
        url : "/family"//对应flask里的路由
    });
};

export function Get_genus(){
    return service.request({
        method : "POST",
        url : "/genus"//对应flask里的路由
    });
};

export function Get_specices(){
    return service.request({
        method : "POST",
        url : "/specices"//对应flask里的路由
    });
};
export function Get_userinfo(userParam){
    return service.request({
        method : "POST",
        url : "/userinfo",
        data :{
            userID : userParam.userID
        }
    });
};

export function Get_alluser(){
    return service.request({
        method : "POST",
        url : "/all_of_users"
    })
};

export function Get_allplant(){
    return service.request({
        method : "POST",
        url : "/all_of_plants"
    })
};

export function Get_allcates(){
    return service.request({
        method : "POST",
        url : "/allcates"
    })
};

export function Get_collection(userid){
    return service.request({
        method : "POST",
        url : "/collection_list",
        data:{
            'user_id': userid
        }
    })
};

export function Get_cates(postParams){
    return service.request({
        method : 'POST',
        url : postParams.url
    })
};

export function Get_one_plant(postParams){
    return service.request({
        method : 'POST',
        url : postParams.url
    })
};

export function Get_one_plant1(postParams){
    return service.request({
        method : 'POST',
        url : "/plant/"+postParams.plant_id
    })
};

export function Add_plant(){
    return service.request({
        method : 'POST',
        url : '/createplant'
    })
};

export function Search_plant(searchParam){
    return service.request({
        method : 'POST',
        url : '/search',
        data:{
            key : searchParam.key
        }
    })
};

export function Reset_userinfo(userParam){
    return service.request({
        method : "POST",
        url : "/modify_userinfo",
        data :{
            userID : userParam.userID,
            new_name : userParam.new_name
        }
    });
};


export function Get_is_collected(collectParam){
    return service.request({
        method : "POST",
        url : "/is_collected",
        data :{
            user_id : collectParam.user_id,
            plant_id : collectParam.plant_id
        }
    });
};


export function Add_a_collection(collectParam){
    return service.request({
        method : "POST",
        url : "/addcollect",
        data :{
            user_id : collectParam.user_id,
            plant_id : collectParam.plant_id
        }
    });
};


export function Del_a_collection(collectParam){
    return service.request({
        method : "POST",
        url : "/delcollect",
        data :{
            user_id : collectParam.user_id,
            plant_id : collectParam.plant_id
        }
    });
};

export function Create_plantinfo(plantParam){
    return service.request({
        method : "POST",
        url : "/createplant",
        data :{
            'pname' : plantParam.PlantName,
            'pchar' : plantParam.Characters,
            'pphy'  : plantParam.Phylum,
            'pcla' : plantParam.Class,
            'pord' : plantParam.Order,
            'pfam' : plantParam.Family,
            'pgen' : plantParam.Genus,
            'pspe' : plantParam.Specices,
            'ploc' : plantParam.Location,
        }
    });
};

export function Modify_plantinfo(plantParam){
    return service.request({
        method : "POST",
        url : "/modify_plantinfo",
        data :{
            'pid' : plantParam.PlantID,
            'pname' : plantParam.PlantName,
            'pchar' : plantParam.Characters,
            'pphy'  : plantParam.Phylum,
            'pcla' : plantParam.Class,
            'pord' : plantParam.Order,
            'pfam' : plantParam.Family,
            'pgen' : plantParam.Genus,
            'pspe' : plantParam.Specices,
            'ploc' : plantParam.Location,
        }
    });
};