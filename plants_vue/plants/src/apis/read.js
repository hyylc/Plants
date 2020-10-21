//请求拦截器
import service from "../utils/request.js"


export function Get_header(){
    return service.request({
        method : "get",
        url : "/plants_header"//对应flask里的路由
    });
};

export function Get_userinfo(){
    return service.request({
        method : "get",
        url : "/userinfo"
    });
};

export function Get_cates(postParams){
    return service.request({
        method : 'POST',
        url : postParams.url//,
        //data:{
          //  key : postParams.key, //newest
            //secretKey : '我是key'
        //}
    })
}