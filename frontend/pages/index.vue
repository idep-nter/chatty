<template>
  <v-container>
    <v-container class="mt-15 d-flex justify-center">
      <v-icon class="ml-5 mr-2 icon" color="primary" x-large> mdi-bird </v-icon>
      <h1>CHA-CHA-CHATTY!</h1>
    </v-container>
    <v-container class="mt-5">
      <div class="d-flex justify-center">
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Alias
          distinctio necessitatibus beatae suscipit quas, non blanditiis,
          provident placeat doloremque harum, quia dolor mollitia recusandae
          perferendis. Dicta ut quis et assumenda.
        </p>
      </div>
    </v-container>
    <v-container class="mt-10">
      <div class="d-flex justify-center chat">
        <NuxtLink to="/threads">
          <h3>Let's chat!</h3>
        </NuxtLink>
      </div>
    </v-container>
  </v-container>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.chat {
  position: absolute;
  bottom: 45%;
  left: 0%;
  right: 0%;
}
h1 {
  color: $primaryColor;
}

p {
  padding: 0px 200px;
}
</style>
