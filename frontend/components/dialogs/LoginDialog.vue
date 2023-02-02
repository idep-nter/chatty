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
      <h1>Log in</h1>
      <v-form ref="form" v-model="valid" lazy-validation class="pa-sm-4">
        <v-text-field
          v-model="username"
          :rules="usernameRules"
          :counter="20"
          label="Username"
          required
        ></v-text-field>

        <v-text-field
          autocomplete="current-password"
          :value="password"
          label="Password"
          :append-icon="value ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="() => (value = !value)"
          :type="value ? 'password' : 'text'"
          :rules="passwordRules"
          @input="(_) => (password = _)"
        ></v-text-field>

        <v-container>
          <v-container class="mt-8 justify-center d-flex">
            <v-btn color="primary" class="mr-4" @click="closeDialog">
              Close
            </v-btn>
            <v-btn
              color="primary"
              :disabled="!valid"
              class="mr-4"
              @click="submitForm"
            >
              Log in
            </v-btn>
            <v-btn color="primary" @click="toggleAuth()" class="mr-4"
              >Register instead</v-btn
            >
          </v-container>
          <v-container class="mt-8 justify-center d-flex">
            <a href="/">Forgot password?</a>
          </v-container>
        </v-container>
      </v-form>
    </v-container>
  </v-card>
</template>

<script>
export default {
  emits: ['toggle-auth', 'close-dialog', 'load-stuff'],
  data() {
    return {
      valid: true,
      value: true,
      password: '',
      passwordRules: [
        (v) => !!v || 'Password is required!',
        (v) =>
          /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$/.test(
            v
          ) ||
          'Password must contain a minimum of eight characters, at least one upper case English letter, one lower case English letter, one number and one special character!',
      ],
      username: '',
      usernameRules: [
        (v) => !!v || 'Username is required!',
        (v) =>
          (v && v.length <= 20) || 'Username must be less than 20 characters!',
      ],
      formData: {},
      errorMessage: '',
    };
  },
  computed: {},
  methods: {
    toggleAuth() {
      this.$emit('toggle-auth');
    },
    closeDialog() {
      this.valid = true;
      this.password = '';
      this.username = '';
      this.$refs.form.resetValidation();
      this.$emit('close-dialog');
    },
    validate() {
      this.$refs.form.validate();
    },
    async submitForm() {
      this.formData = {
        username: this.username,
        password: this.password,
      };

      await this.$store.dispatch('auth/login', this.formData);

      if (this.showError) {
        this.errorMessage = 'Failed to authenticate! Check your login data.';
        return;
      }
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
