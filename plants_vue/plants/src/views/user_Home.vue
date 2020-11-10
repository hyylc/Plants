<template>
  <div class="home">
    <Header />
    <b-container>
      <!-- <div class="background">
        <img :src="imgsrc" width="100%" height="100%" alt=""/>
      </div> -->
      <div class="contain">
            <div class="title">标签查询：</div>
            <div class="bform">
              <p ><span>门:</span><button class="Phylum" type="text" @click="turnto('/Angiospermae')">被子植物门</button><button  class="Phylum" type="text" @click="turnto('/Pteridophyta')">裸子植物门</button><button  class="Phylum" type="text" @click="turnto('/Angiospermae')">蕨类植物门</button></p>
              <p><span>纲:</span><button class="Class" type="text" @click="turnto('/Monocotyledoneae')">单子叶植物纲</button><button  class="Class" type="text" @click="turnto('/Dicotyledoneae')" >双子叶植物纲</button><button class="Class"  type="text" @click="turnto('/Chlamydospermopsida')">盖子植物纲</button><button  class="Class" type="text" @click="turnto('/Coniferopsida')">松杉纲 </button><button  class="Class" type="text" @click="turnto('/Lycopodiinae')">石松纲</button></p>
              <p><span>   </span><button class="Class"  type="text" @click="turnto('/Archichlamydeae')">原始花被亚纲</button><button class="Class"  type="text" @click="turnto('/Sympetalae')" >合瓣花亚纲</button><button  class="Class" type="text" @click="turnto('/Leptosporangiatidae')">薄囊蕨亚纲</button><button  class="Class" type="text" @click="turnto('/Filicopsida')">蕨纲</button></p>
              <p><span>目:</span><button class="Order" type="text" @click="turnto('/Rosales')">蔷薇目</button><button class="Order" type="text" @click="turnto('/Rutales')">芸香目</button><button class="Order" type="text" @click="turnto('/Scitamineae')">芭蕉目</button><button  class="Order" type="text" @click="turnto('/Taxales')">红豆杉目 </button><button class="Order" type="text" @click="turnto('/Arales')">天南星目 </button><button class="Order" type="text" @click="to1">...</button></p>
              <p><span>科:</span><button class="Family" type="text" @click="turnto('/Juncaceae')">灯心草科</button><button class="Family"  type="text" @click="turnto('/Gaultherioideae')">白珠树亚科</button><button   class="Family"   type="text" @click="turnto('/Sabiaceae')">清风藤科</button><button class="Family"  type="text" @click="turnto('/Theaceae')">山茶科 </button><button  class="Family" type="text" @click="turnto('/Melastomataceae')">野牡丹科</button><button  class="Family"  type="text" @click="to2">...</button></p>
              <p><span>属:</span><button class="Genus" type="text" @click="turnto('/Centaurea')">矢车菊属</button><button  class="Genus" type="text" @click="turnto('/Diphasiastrum')">扁枝石松属</button><button  class="Genus" type="text" @click="turnto('/Machilus')">润楠属</button><button  class="Genus" type="text" @click="turnto('/Vicatia')">凹乳芹属</button><button  class="Genus" type="text" @click="turnto('/Magnolia')">木兰属</button><button  class="Genus" type="text" @click="to3">...</button></p>
              <p><span>种:</span><button class="Specices"  type="text" @click="turnto('/Dracaeneae')">龙血树族</button><button  class="Specices" type="text" @click="turnto('/INDIGOFEREAE')">木蓝族 </button><button class="Specices"  type="text" @click="turnto('/Coryphinae')">贝叶棕亚族 </button><button class="Specices"  type="text" @click="turnto('/Lonicereae')">忍冬族</button><button   class="Specices"  type="text" @click="turnto('/Smyrnieae')">美味芹族</button><button class="Specices"  type="text" @click="to4">...</button></p> 
            </div>
      </div>
   </b-container>
    <!-- <Footer /> -->

  </div>
</template>


<script>
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import { Get_allcates } from "../apis/read"


export default {
  name: "home",
  components: {
    Header,
    Footer
  },
    data() {
      return{
        data:[],
        imgsrc: require('../assets/backpic.jpg')
      }
    },
    created() {
      this.user_id = window.sessionStorage.UserID;
      this.getdata()
    },
    	methods: {
          getdata(){
              Get_allcates().then(resp => {
                this.data = resp.data.data
                console.log('输出结果 = ',this.data)
              })
          },
          turnto(plant_type){
            this.$router.push({
                            path:plant_type,
                        });
          },
          to1(){
              this.$router.push({
                            path:'/Order',
                        });
          },
         to2(){
              this.$router.push({
                            path:'/Family',
                        });
          },
         to3(){
              this.$router.push({
                            path:'/Genus',
                        });
          },
         to4(){
              this.$router.push({
                            path:'/Specices',
                        });
          }
        }
};
</script>


<style scoped>
.background{
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  position: absolute;
}
.home{
  width: 100%;
  max-width: 1200px;
  margin: 40px auto;
  padding: 0 20px;
  box-sizing:border-box;
}
.contain{
  z-index: 1;
  position: absolute;
}
.title{
    margin-left: 10px;
		font-size: 2em;
		font-weight: bold; 
		color: #66CDAA;
    opacity: 0.5;
    text-align: "center";
	}
.bform{
		width: 1500px;
		height: 40%;
    margin: 0 auto;
		/*padding: 2em 0;
		 display: flex; */
		/* flex-direction: column;
		justify-content: space-around;
		align-items: center; */

	}
 .Phylum{
    width: 8%;
		height: 25px;
		outline: none;
    margin-left: 6px;
		background-color: #fff;
		color:  rgb(57, 117, 122);
		font-size: 0.9em;
		cursor: pointer;
    text-align: center;
    /* 按钮设置边框 */
    border:1px transparent solid;
    border-radius: 30px;
    border-width: 1.5px;
    border-Color: #B8F1CC;
    }
  .Class{
    width: 8%;
		height: 25px;
		outline: none;
    margin-left: 6px;
		background-color: #fff;
		color:  rgb(57, 117, 122);
		font-size: 0.9em;
		cursor: pointer;
    text-align: center;
    /* 按钮设置边框 */
    border:1px transparent solid;
    border-radius: 30px;
    border-width: 1.5px;
    border-Color: #00bfff;
    }
  .Order{
    width: 8%;
		height: 25px;
		outline: none;
    margin-left: 6px;
		background-color: #fff;
		color:  rgb(57, 117, 122);
		font-size: 0.9em;
		cursor: pointer;
    text-align: center;
    /* 按钮设置边框 */
    border:1px transparent solid;
    border-radius: 30px;
    border-width: 1.5px;
    border-Color: #fa8072;
    }
.Family{
    width: 8%;
		height: 25px;
		outline: none;
    margin-left: 6px;
		background-color: #fff;
		color:  rgb(57, 117, 122);
		font-size: 0.9em;
		cursor: pointer;
    text-align: center;
    /* 按钮设置边框 */
    border:1px transparent solid;
    border-radius: 30px;
    border-width: 1.5px;
    border-Color: #f0b631;
    }
  .Genus{
    width: 8%;
		height: 25px;
		outline: none;
    margin-left: 6px;
		background-color: #fff;
		color:  rgb(57, 117, 122);
		font-size: 0.9em;
		cursor: pointer;
    text-align: center;
    /* 按钮设置边框 */
    border:1px transparent solid;
    border-radius: 30px;
    border-width: 1.5px;
    border-Color: #c86f67;
    }
  .Specices{
    width: 8%;
		height: 25px;
		outline: none;
    margin-left: 6px;
		background-color: #fff;
		color:  rgb(57, 117, 122);
		font-size: 0.9em;
		cursor: pointer;
    text-align: center;
    /* 按钮设置边框 */
    border:1px transparent solid;
    border-radius: 30px;
    border-width: 1.5px;
    border-Color: #20b2aa;
    }
 button{
		width: 8%;
		height: 25px;
		outline: none;
    margin-left: 6px;
		background-color: #fff;
		color:  rgb(57, 117, 122);
		font-size: 0.9em;
		cursor: pointer;
    text-align: center;
    /* 按钮设置边框 */
    border:1px transparent solid;
    border-radius: 30px;
    border-width: 1.5px;
    border-Color: rgb(148, 215, 221);
	}
  p{
        /* text-align: left;
        font-size: 1.2rem;
        /* margin:auto; */
        /* font-weight: bold;
        line-height: 50px; */ 
        padding-left: 200px;
        color: rgb(57,167,176);
    }
   
</style>
