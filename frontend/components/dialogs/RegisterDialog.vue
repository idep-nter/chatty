<template>
  <v-card>
    <v-container>
      <v-alert
        dense
        outlined
        type="error"
        v-if="errorMessage"
        class="justify-center mx-auto mt-15 logAlert"
        max-width="500"
      >
        {{ errorMessage }}
      </v-alert>
      <h1>Register</h1>
      <v-form ref="form" v-model="valid" lazy-validation class="pa-sm-4">
        <v-text-field
          v-model="username"
          :rules="usernameRules"
          :counter="20"
          label="Username"
          required
        ></v-text-field>

        <v-text-field
          v-model="name"
          :rules="nameRules"
          :counter="30"
          label="Name"
          required
        ></v-text-field>

        <v-text-field
          v-model="image"
          :rules="imageRules"
          label="Image URL"
          required
        ></v-text-field>

        <v-text-field
          v-model="email"
          :rules="emailRules"
          label="E-mail"
          required
        ></v-text-field>

        <v-text-field
          autocomplete="current-password"
          :value="password"
          label="Password"
          :append-icon="value ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="() => (value = !value)"
          :type="value ? 'password' : 'text'"
          :rules="pswModeRules"
          @input="(_) => (password = _)"
        ></v-text-field>

        <v-text-field
          autocomplete="current-password"
          :value="password2"
          label="Confirm password"
          :append-icon="value2 ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="() => (value2 = !value2)"
          :type="value2 ? 'password' : 'text'"
          :rules="password2Rule"
          @input="(_) => (password2 = _)"
        ></v-text-field>

        <v-container class="mt-8 justify-center d-flex">
          <a href="/">Forgot password?</a>
        </v-container>
        <v-container class="mt-8 justify-center d-flex">
          <v-btn
            color="primary"
            :disabled="!valid"
            class="mr-4"
            @click="submitForm"
          >
            Sign in
          </v-btn>
          <v-btn color="primary" @click="toggleAuth()" class="mr-4"
            >Log in instead</v-btn
          >
        </v-container>
      </v-form>
    </v-container>
  </v-card>
</template>

<script>
export default {
  emits: ['toggle-auth'],
  data() {
    return {};
  },
  computed: {},
  methods: {
    toggleAuth() {
      this.$emit('toggle-auth');
    },
  },
};
</script>

<style lang="scss" scoped>
h1 {
  display: flex;
  justify-content: center;
  color: $primaryColor;
}

@media (max-width: 767px) {
  .logAlert {
    margin-top: 10px !important;
  }
}
</style>
