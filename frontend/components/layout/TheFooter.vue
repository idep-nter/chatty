<template>
  <v-footer padless>
    <v-col class="text-center" color="grey">
      <p>
      Created by
      <span
        ><a href="https://www.linkedin.com/in/m-sterzinger/" target="_blank"
          >Michael Sterzinger</a
        >
      </span>
      | © 2022 All rights reserved
      </p>
    </v-col>
  </v-footer>
</template>

<style lang="scss"  scoped>
a { 
  text-decoration: none;
  color: $primaryColor;
  font-weight: bold;
}

/* Smartphones */
@media (max-width: 767px) {
  p {
    font-size: 12px;
  }
}
</style>

<script>
</script>