pipeline {
    agent any

    environment {
        IMAGE_NAME = 'pia_back'
        REGISTRY = 'localhost:5000'
        APP_ENV = 'dev'  // Cambia a 'dev' o 'prod' según el entorno
    }

    stages {
        stage('Build and Run Services') {
            steps {
                script {
                    // Asegurarse de que el archivo .env esté disponible
                    sh 'test -f .env.${APP_ENV} || { echo ".env.${APP_ENV} no existe"; exit 1; }'
                    
                    // Construir y levantar los servicios usando el archivo .env del docker-compose.yml
                    sh "docker-compose up -d --build"
                }
            }
        }

        stage('Run Migrations') {
            steps {
                script {
                    // Esperar hasta que la base de datos esté lista y ejecutar las migraciones
                    sh 'docker-compose exec web sh -c "until nc -z db 5432; do echo Waiting for the database; sleep 1; done; python manage.py migrate"'
                }
            }
        }

        stage('Collect Static Files') {
            steps {
                script {
                    // Colectar archivos estáticos (si aplica)
                    sh 'docker-compose exec web python manage.py collectstatic --noinput'
                }
            }
        }

        stage('Tests') {
            steps {
                script {
                    // Ejecutar las pruebas (opcional)
                    sh 'docker-compose exec web python manage.py test'
                }
            }
        }
    }

    post {
        always {
            script {
                // Mostrar los logs en caso de errores
                sh 'docker-compose logs'
            }
        }
    }
}
