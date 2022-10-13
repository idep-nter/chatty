<template>
    <v-row class="mt-12 mainRow d-flex justify-center">
      <v-col md="8" sm="7" class>
        <v-card max-width="1400" height="100" class="pa-2 filterCard"> </v-card>
      </v-col>

      <v-col md="8" sm="7">
        <v-card max-width="1400" height="695" class="pa-2 itemCard">
          <thread-list-item
            v-for="(thread, index) in threads"
            :key="thread.id"
            :id="thread.id"
            :number="index + 1"
            :title="thread.title"
            :lastUpdated="thread.lastUpdated"
            :updatedBy="thread.updatedBy"
          >
          </thread-list-item>

          <v-pagination id="pagination" color="primary"></v-pagination>

          <v-container id="create" class="d-flex justify-center">
            <v-dialog v-model="createThreadDialog" max-width="600px" persistent>
              <template v-slot:activator="{ on, attrs }">
                <v-btn v-bind="attrs" v-on="on" color="primary"
                  >Create Thread</v-btn
                >
              </template>
              <create-thread-dialog
                @save-data="saveData"
                @close-dialog="createThreadDialog = false"
              ></create-thread-dialog>
            </v-dialog>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
</template>

<script>
import ThreadListItem from '~/components/threads/ThreadListItem.vue';
import CreateThreadDialog from '~/components/dialogs/CreateThreadDialog.vue';

export default {
  components: { ThreadListItem, CreateThreadDialog },
  data() {
    return {
      createThreadDialog: false,
      num: 0,
      threads: [],
    };
  },
  created() {
    this.threads = this.$store.getters['threads/getThreads'];
  },
  methods: {},
};
</script>

<style scoped>
/* .bottom {
  align-items: center;
  height: 100%;
} */

li {
  list-style-type: none;
}
#pagination {
  position: absolute;
  bottom: 13%;
  left: 0%;
  right: 0%;
}

#create {
  position: absolute;
  bottom: 3%;
  left: 0%;
  right: 0%;
}

/* a {
    text-decoration: none;
    color: #006400;
  } */

/* Smartphones */
/* @media (max-width: 767px) {
    .itemCard {
      height: 1300px !important;
    }
    .mainRow {
      margin-top: 0px !important;
    }
  }
   */
/* Tablets */
/* @media (min-width: 768px) and (max-width: 991px) {
    .mainRow {
      justify-content: center;
    }
  }
  
  /* Desktop */
/* @media (min-width: 992px) {
    .filterCard {
      margin-left: 25px;
    }
  } */
</style>
