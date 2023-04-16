import Head from 'next/head'
import { Inter } from 'next/font/google'
import styles from '@/styles/Home.module.css'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <>
      <Head>
        <title>TBD Movie Recommendation App</title>
        <meta name="description" content="Generated by create next app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
x

      <main className={styles.main}>
        <div className={styles.description}>
        </div>

        <div className={styles.topcenter}>
          <h1>TBD App</h1>
        </div>

      <div style={{display : 'flex'}}>
        <div className={styles.center}>
            <div className={styles.card}>
              <h2>Movie Title &rarr;</h2>
            </div>
        </div>
      
        
        <div className={styles.center}>
            <div className={styles.card}>
              <h2>Movie Title &rarr;</h2>
            </div>
        </div>
      </div>




      <div style={{display : 'flex'}}>
          <div className={styles.grid}>
            <a
              // href="https://nextjs.org/docs?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
              className={styles.button1}
              target="_blank"
              rel="noopener noreferrer"
            >
              <FontAwesomeIcon icon="fa-solid fa-thumbs-up" />

            </a>

            <a
              className={styles.button2}
              target="_blank"
              rel="noopener noreferrer"
            >
              <FontAwesomeIcon icon="fa-solid fa-question" />

            </a>

            <a
              className={styles.button3}
              target="_blank"
              rel="noopener noreferrer"
            >
              <FontAwesomeIcon icon="fa-solid fa-thumbs-down" />
              {/* <p className={inter.className}>
                Dislike <span>-&gt;</span>
              </p> */}

            </a>
          </div>
        </div>
      </main>
    </>
  )
}
