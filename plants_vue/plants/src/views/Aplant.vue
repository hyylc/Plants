<template>
	<div class="big">	
      <Header />
	  
	  <el-button type="success" @click="creat" style="margin-left:930px;">创建植物</el-button>
		<div class="contain">
        
        <el-table :data="data.slice((page-1)*10, page*10)" border>
            <el-table-column label="植物名">
	   	    <template slot-scope="scope">
			<span>{{scope.row.PlantName}}</span> 
			
	        </template>
			</el-table-column>
            <el-table-column label="操作" prop="operation">
			 <template slot-scope="scope">
		 <el-button type="text" @click="checkDetail(scope.row.PlantID)">查看详情</el-button>
	 <el-button type="text" @click="modifyPlant(scope.row.PlantID)">修改</el-button> 
	<el-button type="text" @click="deletePlant(scope.row.PlantID)">删除</el-button>	
		</template>
		</el-table-column>
        </el-table>
        <div style="text-align: center;">
			<el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange"
			    :current-page="page" :page-sizes="[1, 2,5, 10]" :page-size="limit"
			    layout="total, sizes, prev, pager, next, jumper" :total="total">
			</el-pagination>
		</div>
		</div>
    </div>

</template>


<script>

import Header from "../components/AHeader";
import Footer from "../components/Footer";
import { Get_allplant ,del_plant} from "../apis/read.js"

export default {
	name : "userinfo",
    components:{
        Header,
        Footer
    }, 
		data() {
			
			return {
				data: [], // 显示的数据
				limit: 10, // 条数，每一页显示的数量
				total: 0, // 所有的数量
				page: 1, //当前页
				searchData: '', // 搜索内容
				//data:[]	//接口返回的所有用户信息
			}
		},
		created() {
			//this.pageList();
			this.post_allPlant();
			
		},
		methods: {
			// pageList() {
			// 	this.post_allPlant()
			// },
			mounted() {
            this.post_allPlant();
       		},
			post_allPlant() {
				Get_allplant().then(resp => {
					this.data = resp.data.data
					this.total = resp.data.data.length
					console.log('输出结果 = ',this.data)
				})
			},
			checkDetail(plant_id){
				this.$router.push({
                            path:'/plantA/'+plant_id,
                        });
			},
			creat(){
				this.$router.push({
                            path:'/CreatePlant'
                        });
			},
			modifyPlant(plant_id){
				this.$router.push({
                            path:'/ModifyPlant/'+plant_id,
                        });
			 },
			deletePlant(plant_id){
					// del_user(user_id).{
					// 	this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
					// 	confirmButtonText: "确定",
					// 	cancelButtonText: "取消",
					// 	type: "warning"
					// })
					del_plant(plant_id).then((resp) => {
					// 点击确认删除后向后端发起请求删除该数据
						console.log(resp.data.data);
						this.$message({
							type: "success",
							message: "删除成功!"
						});
					})
			},



			// 处理数据
			// getList() {
			// 	// es6过滤得到满足搜索条件的展示数据list
			// 	var list = this.data.filter((item, index) =>
			// 		item.name.includes(this.searchData)
			// 	) // 搜索符号条件的内容
			// 	console.log(list)
			// 	this.list = list.filter((item, index) =>
			// 		index < this.page * this.limit && index >= this.limit * (this.page - 1)
			// 	) //根据页数显示相应的内容
			// 	this.total = list.length

				/////////
				// var list = this.alluser
				// console.log(list)
				// this.list = list.filter((item, index) =>
				// 	index < this.page * this.limit && index >= this.limit * (this.page - 1)
				// ) //根据页数显示相应的内容
				// this.total = list.length
				////////
			
			// 当每页数量改变
			handleSizeChange(val) {
				console.log(`每页 ${val} 条`);
				this.limit = val
				//post_allPlant()
			},
			// 当当前页改变
			handleCurrentChange(val) {
				console.log(`当前页: ${val}`);
				this.page = val
				//this.getList()
			},
			// 搜索过滤数据
			search() {
				this.page = 1
				//this.getList()
			}
		},
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
	.big{
		width: 100vw;
		height: 100vh;
	}
	.contain{
		width: 60%;
		height: 100%;
		opacity:0.85;
		position: relative;
		top: 50%;
		left: 50%;
		transform: translate(-50%,-50%);
		background-color: #fff;
		border-radius: 20px;
		box-shadow: 0 0 3px #f0f0f0,
					0 0 6px #f0f0f0;
	}
	.big-box{
		width: 100%;
		height: 100%;
		position: absolute;
		top: 0;
		left: 30%;
		transform: translateX(0%);
		transition: all 1s;
	}
	.big-contain{
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
    .btitle{
		font-size: 1.5em;
		font-weight: bold;
        text-align: center;
		color: rgb(57,167,176);
	}
	.bform{
		width: 100%;
		height: 70%;
		padding: 2em 0;
		display: flex;
		flex-direction: column;
		justify-content: space-around;
		align-items: center;
	}
    p{
        text-align: left;
        font-size: 0.2rem;
        margin:auto;
        font-weight: bold;
        color: rgb(57,167,176);
    }
	.bform .errTips{
		display: block;
		width: 50%;
		text-align: left;
		color: red;
		font-size: 0.7em;
		margin-left: 1em;
	}
	.bform .input{
		width: 50%;
		height: 30px;
		border: none;
		outline: none;
		border-radius: 10px;
		padding-left: 2em;
		background-color: #f0f0f0;
	}
	.bbutton{
        display: block;
		width: 20%;
		height: 40px;
		border-radius: 24px;
		border: none;
		outline: none;
		background-color: rgb(57,167,176);
		color: #fff;
		font-size: 0.9em; 
        margin-top: 20px;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
		cursor: pointer;
	}
</style>