//请求拦截器
import service from "../utils/request.js"


export function GetCates(){
    return service.request({
        method : "get",
        url : "/plants_cates"
    })
}