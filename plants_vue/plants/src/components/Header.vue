<template>
    <b-container>
        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand href="#">植物信息检索</b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
                <b-nav-item v-for = "item in headData.headers" :key="item.id" :href= "item.url">{{item.name}}</b-nav-item>
            </b-navbar-nav>

            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">
                <b-nav-form>
                <b-form-input size="sm" class="mr-sm-2" placeholder="输入植物名称"></b-form-input>
                <b-button size="sm" class="my-2 my-sm-0" type="submit">搜索</b-button>
                </b-nav-form>
            </b-navbar-nav>
            
            </b-collapse>
        </b-navbar>
    </b-container>
</template>

<script>
import { Get_header } from "../apis/read.js";//从apis中引入，通过这个请求拿到数据
import { reactive, ref } from "@vue/composition-api";//ref定义常量;reactive定义对象

export default {
    name : "Header",
    setup(props, context){ //setup相当于before create;props父组件传入的内容;context当前组件拥有的内容
        const headData = reactive({
            headers:[]
        });

        Get_header().then(Response =>{
            console.log("In Header Response = ",Response)//得到返回结果response
            headData.headers = Response.data.data;
            console.log("headData.headers = ",headData.headers)
        });

        return {
            headData
        }
    }
}
</script>

<style lang='scss' scoped>//lang告诉解释其css符合什么编译器的语法；scoped：当前vue文件生效，没有scoped则全局生效

</style>