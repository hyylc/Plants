//请求拦截器
import service from "../utils/request.js"


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

export function Get_userinfo(userParam){
    return service.request({
        method : "POST",
        url : "/userinfo",
        data :{
            userID : userParam.userID
        }
    });
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
export function Reset_userpwd(userParam){
    return service.request({
        method : "POST",
        url : "/modify_pwd",
        data :{
            userID : userParam.userID,
            new_pwd : userParam.newuserpwd
        }
    });
};