pipeline {
 agent any
 stages {
  stage("test") {
   steps {
       git 'https://github.com/aviz90/devops.git'
    script {
     try {
      echo 'do your stuff'
     } catch (Exception e) {
      echo 'Handle the exception!'
     }
    }
   }
  }
  
 }
}
