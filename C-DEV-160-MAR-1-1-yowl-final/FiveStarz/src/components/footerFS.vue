<template>
<div class="">
  <footer
    class="
      sticky
      inset-x-0
      bottom-0
      lg:mx-10
      lg:rounded-lg
      flex flex-row
      justify-between
      items-end
      lg:px-10
      lg:h-16
      h-10
      text-white
      bg-blue-800
      rounded-md
      footer
      mx-10
    ">
    <a href="/Admin"
      ><img
        src="@/assets/FIVE_STARZ_FOOTER.png"
        class="lg:h-20 logo_bottom lg:pt-5 mx-24 pt-3"
        title="Best of reviews"
    /></a>
    <p class="invisible lg:pb-5 lg:visible">
      © Benoit Berlanger, Baptiste Cardoso, Magda Hennebo, Chrystal Tiran
    </p>
    <div  class="lg:pb-5">
    <a class="lg:pr-5 lg:visible invisible" href="#">Careers</a
    ><a class="lg:pr-5 lg:visible invisible" href="#">Privacy notice</a
    ><a class="lg:text-base lg:visible invisible" href="#">Contact us</a>
    </div>
  </footer></div>
</template>

<script>
export default {}
</script>

<style>
footer {
  font-family: "Raleway";
}
@media screen and (max-width: 1080px)
{
  .footer {
    width: 295px;
  }
  .logo_bottom {
    height: 50px;
  }
}
</style>
