import time
import random
from queue import Queue
from threading import Thread
from dataclasses import dataclass


@dataclass
class Request:
    id: int
    text: str

class Producer:
    def __init__(self, queue: Queue):
        self._num_generated_requests: int = 0
        self._queue: Queue = queue

    def _generate_request(self) -> None:
        request: Request = Request(
            id=self._num_generated_requests, text='request text'
        )

        self._queue.put(request)

        print(
            f'Producer: request (id: {request.id}) '
            'successfully generated and put to the queue.'
        )

        time.sleep(random.uniform(a=0.0, b=2.0))
        self._num_generated_requests += 1

    def generate_requests(self) -> None:
        while True:
            self._generate_request()


class Consumer:
    def __init__(self, queue: Queue):
        self._num_processed_requests: int = 0
        self._queue: Queue = queue

    def _process_request(self) -> None:
        if not queue.empty():
            request: Request = queue.get()
            time.sleep(random.uniform(a=0.0, b=2.0))

            print(
                f'Consumer: request (id: {request.id}) '
                'successfully extracted from the queue and processed.'
            )

            self._num_processed_requests += 1

        else:
            print('Queue is empty.')
            time.sleep(random.uniform(a=0.0, b=0.5))

    def process_requests(self) -> None:
        while True:
            self._process_request()
           

if __name__ == '__main__':
    queue: Queue = Queue(maxsize=100)

    consumer: Consumer = Consumer(queue=queue)
    producer: Producer = Producer(queue=queue)

    consumer_thread: Thread = Thread(target=consumer.process_requests, daemon=True)
    producer_thread: Thread = Thread(target=producer.generate_requests, daemon=True)

    print('To stop a simulation press Ctrl+C \n')
    time.sleep(2)
    
    try:
        consumer_thread.start()
        producer_thread.start()

        producer_thread.join()
        consumer_thread.join()

    except (KeyboardInterrupt, SystemExit):
        print('\nExit')