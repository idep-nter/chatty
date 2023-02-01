<template>
  <v-row class="mt-12 mainRow d-flex justify-center">
    <v-col md="8" sm="7" class>
      <v-card max-width="1400" height="100" class="pa-2 filterCard">
        <v-row>
          <v-col cols="4">
            <v-text-field
              dense
              class="ml-5 mt-6"
              prepend-icon="mdi-magnify"
              flat
              outlined
              placeholder="Search by name"
              filled
              v-model="searchedName"
            ></v-text-field>
          </v-col>

          <v-col cols="3">
            <v-autocomplete
              class="mt-6"
              v-model="searchedTags"
              :items="tagNames"
              filled
              outlined
              dense
              chips
              small-chips
              label="Search by tags"
              multiple
            ></v-autocomplete>
          </v-col>
          <v-col cols="3">
            <v-container id="dropdown-example-1">
              <v-overflow-btn
                filled
                v-model="sortBy"
                dense
                class="sortBy"
                :items="sorts"
                label="Sort by"
              ></v-overflow-btn>
            </v-container>
          </v-col>
          <v-col cols="2">
            <v-container class="px-0" fluid>
              <v-checkbox
                v-model="showMyThreads"
                label="My Threads"
              ></v-checkbox>
            </v-container>
          </v-col>
        </v-row>
      </v-card>
    </v-col>

    <v-col md="8" sm="7">
      <v-card max-width="1400" height="695" class="pa-2 itemCard">
        <thread-list-item
          v-for="(thread, index) in filteredThreads"
          :key="thread.id"
          :id="thread.id"
          :number="index + 1"
          :title="thread.name"
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
      sorts: ['Alphabetically', 'Last updated'],
      sortBy: '',
      searchedName: '',
      tagNames: [],
      tags: [],
      searchedTags: [],
      showMyThreads: false,
      createThreadDialog: false,
      num: 0,
      threads: [],
      currentUserId: '',
    };
  },
  created() {
    this.loadThreads();
    this.loadTags();
    this.getTagNames();
    this.$store.dispatch('threads/loadPosts');
    // this.$store.dispatch('users/loadUsers');
    this.currentUserId = this.$store.getters['users/getUserId'];
    console.log;
  },
  computed: {
    filteredThreads() {
      // filter by name
      let filtered = this.threads.filter((thread) => {
        return thread.name
          .toLowerCase()
          .includes(this.searchedName.toLowerCase());
      });

      // filter my threads
      if (this.showMyThreads) {
        const myThreads = this.getMyThreads();
        filtered = filtered.filter((thread) => {
          return myThreads.includes(thread.id);
        });
      }

      // filter by tags
      if (this.searchedTags.length !== 0) {
        const tagIds = [];
        this.searchedTags.forEach((tag) => {
          const tagId = this.$store.getters['threads/getTagByName'](tag).id;
          tagIds.push(tagId);
        });
        filtered = filtered.filter((thread) => {
          return thread.tags.some((tag) => tagIds.includes(tag));
        });
      }

      // sort
      if (this.sortBy == 'Alphabetically') {
        filtered.sort((a, b) => {
          let ta = a.name.toLowerCase(),
            tb = b.name.toLowerCase();

          if (ta < tb) {
            return -1;
          }
          if (ta > tb) {
            return 1;
          }
          return 0;
        });
      } else if (this.sortBy == 'Last updated') {
        filtered.sort((a, b) => {
          let da = new Date(a.lastUpdated),
            db = new Date(b.lastUpdated);
          return da - db;
        });
      }

      return filtered;
    },
  },
  methods: {
    async loadThreads() {
      this.$store.dispatch('threads/loadThreads');
      this.threads = this.$store.getters['threads/getThreads'];
    },
    async loadTags() {
      this.$store.dispatch('threads/loadTags');
      this.tags = this.$store.getters['threads/getTags'];
    },
    getTagNames() {
      this.tagNames = this.tags.map(function (tag) {
        return tag.name;
      });
    },
    getMyThreads() {
      const myThreads = [];
      this.threads.forEach((thread) => {
        const posts = this.$store.getters['threads/getThreadPosts'](thread.id);
        console.log(posts);
        posts.every((post) => {
          if (post.author === this.currentUserId) {
            // NEEED CHECK
            myThreads.push(thread.id);
            return false;
          }
        });
      });
      return myThreads;
    },
  },
};
</script>

<style scoped>
.sortBy {
  margin-top: 10px;
}
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
