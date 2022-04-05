<template>
    <div class="d-flex flex-column mb-3 shadow-lg bg-light rounded" 
    style="width: 200px; height: 250px;">        
        <div class="fs-2 " id="title">Title</div>
        <div class="m-2">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Commodi, recusandae?</div>
        <button type="button" 
            class="rounded-circle me-2 btn btn-outline-secondary 
            align-self-end">+</button>
        <div @click="increment">{{ total }}</div>
    </div>
   
    <div class="d-flex flex-column mb-3 shadow-lg bg-light rounded" 
    style="width: 600px; height: 250px">        
        <div class="fs-2 " id="title">Title</div>
        <div class="m-2">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Commodi, recusandae?</div>
        <button type="button" 
            class="rounded-circle me-2 btn btn-outline-secondary 
            align-self-end">-</button>
      
    </div>
</template>

<script>
export default {
    name : 'PostIt',    
    data(){
        return{
            total: 0 
        }
    },
    methods: {
        increment(){
            this.total += 1
        }
    }   
}
</script>

<style scoped>
#title{
    color: rgba(172, 72, 163, 0.664);
}

</style>