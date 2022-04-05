<template>
    <div>
      <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;700&display=swap" rel="stylesheet">
      <a href="/"
          ><img
            src="@/assets/LOGO_FIVE_STARZ.png"
            class="h-28 logo relative"
            title="Best of reviews"
        /></a>
      <PanelAdmin />
      <footerFS />
    </div>
</template>

<script>
import footerFS from '@/components/footerFS.vue'
import PanelAdmin from '@/components/PanelAdmin.vue'

export default {
  name: 'Admin',
  components: {
    footerFS, PanelAdmin
  }
}
</script>

<style>
</style>
