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
      <h1>
        {{ authTypeSwitch }}
      </h1>
      <v-form ref="form" v-model="valid" lazy-validation class="pa-sm-4">
        <v-text-field
          v-model="username"
          :rules="usrModeRules"
          :counter="showCounter"
          label="Username"
          required
        ></v-text-field>

        <v-text-field
          v-model="email"
          :rules="emailRules"
          label="E-mail"
          required
          v-if="this.isLogin === false"
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
          v-if="this.isLogin === false"
          autocomplete="current-password"
          :value="password2"
          label="Confirm password"
          :append-icon="value2 ? 'mdi-eye' : 'mdi-eye-off'"
          @click:append="() => (value2 = !value2)"
          :type="value2 ? 'password' : 'text'"
          :rules="password2Rule"
          @input="(_) => (password2 = _)"
        ></v-text-field>

        <v-container v-if="this.isLogin === true">
          <v-container class="mt-8 justify-center d-flex">
            <v-btn
              color="primary"
              :small="buttonSize"
              :disabled="!valid"
              class="mr-4"
              @click="submitForm"
            >
              Log in
            </v-btn>
            <v-btn
              color="primary"
              @click="toggleAuth()"
              :small="buttonSize"
              class="mr-4"
              >Sign up instead</v-btn
            >
          </v-container>
          <v-container class="mt-8 justify-center d-flex">
            <a href="/">Forgot password?</a>
          </v-container>
        </v-container>
        <v-container class="mt-8 justify-center d-flex" v-else>
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
    data() {
      return {
        isLogin: true,
      };
    },
    computed: {
      authTypeSwitch() {
        if (this.isLogin === true) {
          return "Login";
        } else {
          return "Register";
        }
      },
    },
    methods: {
      toggleAuth() {
        this.isLogin = this.isLogin ? false : true;
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
  