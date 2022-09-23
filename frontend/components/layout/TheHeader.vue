<template>
  <v-card height="30px">
    <v-toolbar extend>
      <NuxtLink to="/" class="links">
        <v-row class="mr-1">
          <v-icon class="ml-5 mr-2 icon" medium> mdi-bird </v-icon>
          <v-toolbar-title class="headline font-weight-bold">{{
            title
          }}</v-toolbar-title>
        </v-row>
      </NuxtLink>
      <v-breadcrumbs :items="breadcrumbs">
        <template v-slot:item="{ item }">
          <v-breadcrumbs-item :href="item.href" :disabled="item.disabled">
            {{ item.text.toUpperCase() }}
          </v-breadcrumbs-item>
        </template>
      </v-breadcrumbs>
      <v-spacer></v-spacer>

      <div class="right">
        <template v-if="loggedIn">
          <div class="text-center">
            <v-menu offset-y>
              <template v-slot:activator="{ on, attrs }">
                <v-card
                  class="portrait"
                  img="https://placekitten.com/600/600"
                  height="50"
                  width="50"
                  v-bind="attrs"
                  v-on="on"
                ></v-card>
              </template>
              <v-list>
                <v-list-item
                  v-for="(item, index) in items"
                  :key="index"
                  @click="handleClick(index)"
                >
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </div>

          <v-dialog v-model="logoutDialog" max-width="320">
            <layout-the-dialog @disagree="closeDialog" @agree="logout"
              >>
              <template v-slot:text> Do you really want to logout? </template>
            </layout-the-dialog>
          </v-dialog>
        </template>

        <v-dialog v-model="loginDialog" max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn v-bind="attrs" v-on="on" color="primary" :small="true"
              >Sign in</v-btn
            >
          </template>

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
              <v-form
                ref="form"
                v-model="valid"
                lazy-validation
                class="pa-sm-4"
              >
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
        </v-dialog>
      </div>
    </v-toolbar>
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      loginDialog: false,
      logoutDialog: false,
      isLogin: true,
      items: [
        {
          title: "Profile",
          click() {
            this.$router.push("/profile");
          },
        },
        {
          title: "Settings",
          click() {
            this.$router.push("/settings");
          },
        },
        {
          title: "Logout",
          click() {
            this.dialog = true;
          },
        },
      ],
      breadcrumbs: [
        {
          text: "Test1",
          disabled: false,
          href: "auth/login",
        },
        {
          text: "Test2",
          disabled: false,
          href: "auth/login",
        },
        {
          text: "Test2",
          disabled: false,
          href: "auth/login",
        },
      ],
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
    loggedIn() {
      // return this.$store.getters['auth/loggedIn'];
      return false;
    },
    title() {
      switch (this.$vuetify.breakpoint.name) {
        case "xs":
          return "C";
        default:
          return "CHATTY";
      }
    },
  },
  methods: {
    logout() {
      this.dialog = false;
      // this.$store.dispatch('auth/logout');
      this.$router.replace("/");
    },
    closeDialog() {
      this.dialog = false;
    },
    handleClick(index) {
      this.items[index].click.call(this);
    },
    toggleAuth() {
      this.isLogin = this.isLogin ? false : true;
    },
  },
};
</script>

<style lang="scss" scoped>
.links {
  text-decoration: none;
  color: $primaryColor;
}
.icon {
  color: $primaryColor;
}

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
