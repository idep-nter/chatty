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
          v-model="email"
          :rules="emailRules"
          label="E-mail"
          required
        ></v-text-field>

        <v-text-field
          v-model="image"
          :rules="imageRules"
          label="Image URL"
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
            :small="buttonSize"
            class="mr-4"
            @click="closeDialog"
          >
            Close
          </v-btn>
          <v-btn
            color="primary"
            :disabled="!valid"
            class="mr-4"
            @click="submitForm"
          >
            Register
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
  emits: ['toggle-auth', 'close-dialog', 'register-auth'],
  data() {
    return {
      valid: true,
      value: true,
      // value2: true,
      password: '',
      passwordRules: [
        (v) => !!v || 'Password is required!',
        (v) =>
          /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$/.test(
            v
          ) ||
          'Password must contain a minimum of eight characters, at least one upper case English letter, one lower case English letter, one number and one special character!',
      ],
      password2: '',
      password2Rule: [
        (v) => !!v || 'Password is required!',
        (v) => v === this.password || 'Passwords must be the same!',
      ],
      username: '',
      usernameRules: [
        (v) => !!v || 'Username is required!',
        (v) =>
          (v && v.length <= 20) || 'Username must be less than 20 characters!',
      ],
      name: '',
      nameRules: [
        (v) => !!v || 'Name is required!',
        (v) => (v && v.length <= 30) || 'Name must be less than 30 characters!',
      ],
      image: '',
      imageRules: [
        (v) =>
          /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)/.test(
            v
          ) || 'Must be a valid URL',
      ],
      email: '',
      emailRules: [
        (v) => !!v || 'E-mail is required!',
        (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid!',
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
      this.$emit('close-dialog');
    },
    validate() {
      this.$refs.form.validate();
    },
    submitForm() {
      this.validate();

      if (!this.valid) {
        return;
      }

      this.formData = {
        username: this.username,
        name: this.name,
        image: this.image,
        email: this.email,
        password: this.password,
      };

      this.$emit('register-auth', this.formData);

      if (this.showError) {
        this.errorMessage = 'Something went wrong! Please try again later.';
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
