<template>
     <div class="container">
       <form v-on:submit.prevent="register2">
           <fieldset>
               <legend>Especifique lo que desea vender</legend>
               <label> Id del producto</label>
               <input type="number" v-model="dat.id_producto" >
               <label>Nombre Del Producto</label>
               <input type="text" v-model="dat.nombre_producto" placeholder="Nombre Claro del Producto"><br>
               <label>Cantidad del Producto</label>
               <input placeholder="Cantidad" type="number" v-model="dat.cantidad_producto">
               <label >Precio Del producto</label>
               <input placeholder="$Valor$" type="number" v-model="dat.precio_unidad"><br>
             
               <label>Descripcion</label>
               <b-form-textarea
      id="textarea"
      placeholder="Caracteristicas del articulo..."
      rows="3"
      max-rows="3"
      v-model="dat.descripcion"
    ></b-form-textarea>
     <b-form-file
      v-model="dat.images"
      :state="Boolean(dat.images)"
      placeholder="Choose a file..."
      drop-placeholder="Drop file here..."
    ></b-form-file>
        <div class="mt-3">Selected file: {{ dat.images ? dat.images.name : '' }}</div>
           </fieldset>
                 <button btn btn-primary>Registrar Producto</button>

       </form>
    </div>
</template>
<script>
import { mapGetters} from 'vuex'
export default {
 
    data() {
      return {
          dat:{
              id_producto:null,
              nombre_producto:null,
              cantidad_producto:null,
              precio_unidad:null,
              descripcion:null,
              images: null,
           
           
     
      },
      oferta:{
        productoz:null,
        clientez:null,
        ofertaz:"10101",
        booleano:true

      }}
    },computed:{
    ...mapGetters([
         'profile',
         'getProducts'
       ]),
  },
     methods:{
       
         register2(){
          this.$store.dispatch('api_photos',this.dat)
          .then(response =>{
            })
           
             
         },
         registraOferta(){
          this.oferta.productoz = this.dat.id_producto
          this.oferta.clientez = this.profile.cedula
          this.$store.dispatch('api_oferta',this.oferta)
          .then(response =>{
            alert('Se registro todo bien')
          })

         },
         registra1(){
           this.$store.dispatch('api_oferta1',this.oferta.booleano)
           .then(res =>{

           })
         }
  },
  
  }
 

</script>
<style>

</style>
